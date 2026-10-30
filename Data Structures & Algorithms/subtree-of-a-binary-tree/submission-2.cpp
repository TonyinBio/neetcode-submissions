/**
 * Definition for a binary tree tree1.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr && subRoot == nullptr) {
            return true;
        } else if (root == nullptr || subRoot == nullptr) {
            return false;
        } 

        if (equal(root, subRoot)) return true;

        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    bool equal(TreeNode* tree1, TreeNode* tree2) {
        // base cases
        if (tree1 == nullptr && tree2 == nullptr) {
            return true;
        } else if (tree1 == nullptr || tree2 == nullptr) {
            return false;
        } 

        return (tree1->val == tree2->val && 
            equal(tree1->left, tree2->left) &&
            equal(tree1->right, tree2->right));
    }
};
