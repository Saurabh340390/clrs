// This use chaining method for collision resolving
// However, the keys used will contained within limitation 
// of number of slot in hash table, i.e. n = O(m)
// Saurabh Verma 
// clrs problem
#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#define SIZE 10
#define hash_value(v) v%10
struct element_t;
typedef struct element_t{
    char free;
    union
    {
        struct {
            struct element_t *next;
            int value;
        } used;
        struct {
           struct element_t *next;
           struct element_t *prev;
        } empty;
    };
    
}element_t;

typedef struct {
    element_t buckets[SIZE];
    element_t free_list;
} hash_t;

int Hash(int val){
    return hash_value(val);
}

/*helper function*/
void remove_from_free_list(hash_t *hash, element_t *element){
    element->empty.prev->empty.next = element->empty.next;
    element->empty.next->empty.prev = element->empty.prev;
    element->free = 0;
}
 void return_to_free_list(hash_t *hash, element_t *element){
    element_t *sentinel = &(hash->free_list);
    element->free = 1;
    element->empty.prev = sentinel;
    element->empty.next = sentinel->empty.next;
    sentinel->empty.next = element;
    sentinel->empty.next->empty.prev = element;
 }

element_t *allocate(hash_t *hash){
    element_t *element = hash->free_list.used.next;
    assert(element != &(hash->free_list));
    remove_from_free_list(hash, element);
    return element;
}

void reallocate(hash_t *hash, element_t *element){
    int index = Hash(element->used.value);
    element_t *location = &(hash->buckets[index]);
    assert(!location->free);
    element_t *new = allocate(hash);
    new->used.value = element->used.value;
    new->used.next = element->used.next;
    while(location->used.next !=element ){
        location = location->used.next;
        assert(location);
        assert(!location->free);
    }
    location->used.next = new;
}

/* interface */
hash_t *make_hash(){
    hash_t *hash = malloc(sizeof(hash_t));
    hash->free_list.empty.next = hash->buckets;
    hash->free_list.empty.prev = hash->buckets + SIZE;
    element_t *current = &(hash->free_list);
    current->free = 1;
    for(int i=0; i<SIZE; i++){
        element_t *next = &(hash->buckets[i]);
        next->free = 1;
        current->empty.next = next;
        next->empty.prev = current;
        current = next;
    }
    current->empty.next = &(hash->free_list);
    hash->free_list.empty.prev = current;
    return hash;
}

void insert(hash_t *hash, int value){
    int index = Hash(value);
    element_t *location = &(hash->buckets[index]);
    if(location->free){
        remove_from_free_list(hash, location);
        location->used.value = value;
        location->used.next = NULL;
    }
    else if(Hash(location->used.value)==index){
        element_t *element = allocate(hash);
        element->used.value = value;
        element->used.next = location->used.next;
        location->used.next = element;
    }
    else{
        reallocate(hash, location);
        location->used.value=value;
        location->used.next = NULL;
    }
}

element_t *search(hash_t *hash, int value){
    int index = Hash(value);
    element_t *element = &(hash->buckets[index]);
    while(element && !element->free){
        if(element->used.value == value){
            return element;
        }
        element = element->used.next;
    }
    return NULL;
}

void delete(hash_t *hash, int value){
    int index = Hash(value);
    element_t *element = &(hash->buckets[index]);
    if(element->free ||  Hash(element->used.value)!=index) // either free element or host element of other slot
    { return;}

    
    while(element->used.value == value) // we choose to delete all the element with value 'value'
    {
        element_t *next = element->used.next;
        if (next){
            assert(!next->free);
            assert(Hash(next->used.value)==index);
            element->used.next = next->empty.next;
            element->used.value = next->used.value;
            return_to_free_list(hash, next);
        }
        else{
            return_to_free_list(hash, element);
            return;
        }
    }
    element_t *current = element;
    
    while(current->used.next){
        element_t *next = current->used.next;
        assert(!next->free);
        assert(Hash(next->used.value)==index);
        if (next->used.value==value){
            current->used.next = next->used.next;
            return_to_free_list(hash, next);
        }
        else{
            current = next;
        }
}
}
/* debug */
void print_hash(hash_t *hash){
    int free_slot = 0;
    element_t *item = hash->free_list.empty.next;
    while(item !=&(hash->free_list)){
        free_slot++;
        item = item->empty.next;
    }
    printf("number of free slots :%d\n",free_slot);
    for(int i =0; i<SIZE; i++){
        element_t *element = &(hash->buckets[i]);
        printf("    +------+\n");
        printf(" %-2d | ", i);
        if(element->free){
            printf("     |");
        }
        else{
            int foreign = Hash(element->used.value) != i;
            printf("%1s %2d |", (foreign? "/": " "), element->used.value);
            
            if(!foreign){
                while(element->used.next){
                    printf(" -> ");
                    element =  element->used.next;
                    if(element->free){
                        printf("!!FREE");
                        break;
                    }
                    printf("%2d", element->used.value);
                }

            }
        }printf("\n");
}
    printf("    +------+");
    printf("\n\n"); 
}
int main(){
    hash_t *hash1 = make_hash();
    insert(hash1, 10);
    insert(hash1, 11);
    insert(hash1, 12);
    insert(hash1, 14);
    insert(hash1, 22);
    insert(hash1, 11);
    insert(hash1, 11);
    delete(hash1, 11); 
    delete(hash1, 22); 
    delete(hash1, 12);
    element_t *ptr = search(hash1, 11);
    if(ptr){
        printf("%d\n",ptr->used.value);
    }
    else{
        printf("Not found\n");
    }
    print_hash(hash1);
    return 0;
}