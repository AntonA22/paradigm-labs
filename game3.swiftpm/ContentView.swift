import SwiftUI

struct ContentView: View {
    @State private var leftDiceImage = "1"
    @State private var rightDiceImage = "2"
    
    let diceImages = ["1", "2", "3", "4", "5", "6"]
    
    var body: some View {
        ZStack {
            Image("fon1") // Название изображения для фона
                .resizable()
                .aspectRatio(contentMode: .fill)
                .edgesIgnoringSafeArea(.all)
            
            VStack {
                Text("Игра Кости")
                    .font(.custom("Marker Felt", size: 70))
                    .padding(.top, 70)
                
                HStack {
                    Spacer()
                    Image(leftDiceImage) // Название изображения для первой кости
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 125, height: 125)
                        .padding(.trailing, 70)
                        .padding(.top, 70)
                    
                    Image(rightDiceImage) // Название изображения для второй кости
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 125, height: 125)
                        .padding(.leading, 20)
                        .padding(.top, 70)
                    Spacer()
                }
                
                Button(action: {
                    // Действие, выполняемое при нажатии кнопки "Play"
                    leftDiceImage = diceImages[Int.random(in: 0...5)]
                    rightDiceImage = diceImages[Int.random(in: 0...5)]
                }) {
                    Text("Play")
                        .font(.custom("Marker Felt", size: 70))
                        .foregroundColor(.white)
                        .padding()
                        .background(Color.gray)
                        .cornerRadius(10)
                        .padding(.top, 70)
                }
                
                Spacer()
            }
            .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
