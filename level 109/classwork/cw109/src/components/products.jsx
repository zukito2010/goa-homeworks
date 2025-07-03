const Product = ({ productInfo }) => {
    return (
        <>
            <div>
                <img src={productInfo.image} alt="" />
                <h1>{productInfo.title}</h1>
                <p>{productInfo.category}</p>
                <p>{productInfo.price}</p>
            </div>
        </>
    )
}

export default Product;