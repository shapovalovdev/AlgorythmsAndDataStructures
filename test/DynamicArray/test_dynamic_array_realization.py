from  src.DynamicArray.dynamic_array_realization import DynArray
import unittest

class TestDynArray(unittest.TestCase):
    def test_insert_into_empty_array(self):
        da=DynArray()
        
        
        with self.assertRaises(IndexError) as context:
            da.insert(10,5)

        self.assertTrue('Index is out of bounds' in str(context.exception))
    #insert buffer is not changed
    def test_insert_into_array(self):
        da=DynArray()
        for i in range(10):
            da.append(i)
        self.assertEqual(da.count,10, "After insert there is 11 elements")
        self.assertEqual(da.capacity,16, "Capacity is default")
        da.insert(3,777)
        self.assertEqual(da.capacity,16, "Capacity is default after insert")
        self.assertEqual(da.count,11, "After insert there is 11 elements")
        self.assertEqual(da[3],777,"The 3d element is 777")

    def test_insert_into_array_and_resize(self):
        da=DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(da.count,16, "After insert there is 11 elements")
        self.assertEqual(da.capacity,16, "Capacity is default")
        self.assertEqual(da[15],15, "The element in 15th cell is 16 ")
        da.insert(3,777)
        self.assertEqual(da.capacity,32, "Capacity is default after insert")
        self.assertEqual(da.count,17, "After insert there is 11 elements")
        self.assertEqual(da[3],777,"The  element in 3d cell is 777")
        self.assertEqual(da[16],15, "The last element is 16 in the cell")

    def test_insert_into_array_in_the_end_and_resize(self):
        da=DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(da.count,16, "After insert there is 11 elements")
        self.assertEqual(da.capacity,16, "Capacity is default")
        self.assertEqual(da[15],15, "The element in 15th cell is 16 ")
        da.insert(16,777)
        self.assertEqual(da.capacity,32, "Capacity is default after insert")
        self.assertEqual(da.count,17, "After insert there is 11 elements")
        self.assertEqual(da[16],777,"The  element in 3d cell is 777")
        self.assertEqual(da[15],15, "The last element is 15 in the cell")

    def test_insert_into_beginning(self):
        da=DynArray()
        for i in range(5):
            da.append(i)
        da.insert(0,-1)
        self.assertEqual(da.count,6, "After insert there is 6 elements")
        self.assertEqual(da.capacity,16, "Capacity is default")
        self.assertEqual(da[5],4)
        self.assertEqual(da[0],-1,)


    def test_insert_out_of_bounds(self):
        da=DynArray()
        for i in range(5):
            da.append(i)
        
        with self.assertRaises(IndexError) as context:
            da.insert(10,5)

        self.assertTrue('Index is out of bounds' in str(context.exception))

    def test_delete_from_empty_list(self):
        da=DynArray()      
        
        with self.assertRaises(IndexError) as context:
            da.delete(3)

        self.assertTrue('Index is out of bounds' in str(context.exception))

    def test_delete_from_out_of_bound(self):
        da=DynArray()
        for i in range(5):
            da.append(i) 
        
        with self.assertRaises(IndexError) as context:
            da.delete(6)

        self.assertTrue('Index is out of bounds' in str(context.exception))

        with self.assertRaises(IndexError) as context:
            da.delete(-100)

        self.assertTrue('Index is out of bounds' in str(context.exception))


    def test_delete_from_the_beginning_with_shrink_minimal(self):
        da=DynArray()      
        for i in range(5):
            da.append(i)
        self.assertEqual(da.count,5, "There is 5 elements")
        self.assertEqual(da.capacity,16, "Capacity is 16 elements")
        da.delete(0)
        self.assertEqual(da.count,4, "After delete there is 4 elements")
        self.assertEqual(da.capacity,16, "Capacity was not shrinked because there min 16 elements")
        self.assertEqual(da[0],1)
        self.assertEqual(da[3],4)

    def test_delete_from_the_middle_with_shrink(self):
        da=DynArray()      
        for i in range(17):
            da.append(i)
        self.assertEqual(da.count,17, "There is 17 elements")
        self.assertEqual(da.capacity,32, "Capacity is 32 elements")
        da.delete(5)
        self.assertEqual(da.count,16, "After delete there is 16 elements")
        self.assertEqual(da.capacity,32, "Capacity was not shrinked because 16 < 16 == False")
        self.assertEqual(da[5],6)
        self.assertEqual(da[15],16)
        with self.assertRaises(IndexError) as context:
            da[16]

        self.assertTrue('Index is out of bounds' in str(context.exception))
        da.delete(10)
        self.assertEqual(da.count,15)
        self.assertEqual(da.capacity,21, "Capacity was  shrinked to 21 because 15 < 16 == True")
        self.assertEqual(da[10],12)
        self.assertEqual(da[14],16)
        self.assertEqual(da[0],0)
        with self.assertRaises(IndexError) as context:
            da[15]

        self.assertTrue('Index is out of bounds' in str(context.exception))
    
